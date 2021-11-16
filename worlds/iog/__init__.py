from randomizer.classes import World as _IoGWorld
from randomizer.models.randomizer_data import RandomizerData

from ..AutoWorld import World
from ..generic.Rules import add_rule, set_rule

from BaseClasses import Item, Region, Entrance, Location, MultiWorld, ItemClassification

import typing

ITEM_ID_MOVE = 46000
LOCATION_ID_MOVE = 46000


class IoGItem(Item):
    game: str = "Illusion of Gaia"


class IoGLocation(Location):
    game: str = "Illusion of Gaia"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


def _generate_name_to_ids():
    _tmp_world = _IoGWorld(RandomizerData())
    item_name_to_id = dict()
    location_name_to_id = dict()
    for _id, _item_data in _tmp_world.item_pool.items():
        _quantity, _type, _code, _name, _use_inv, _is_prog = _item_data
        if _id == 508:
            _name = "Sky Garden: Map 82 SE Switch"
        if _name == "Hieroglyph":
            _name = f"Hieroglyph{_id - 29}"
        item_name_to_id[_name] = ITEM_ID_MOVE + _id

    for _id, _loc_data in _tmp_world.item_locations.items():
        (_l_region, _l_type, _l_filled_flag, _l_filled_item,
         _l_restricted_items, _l_item_addr, _l_text_addr, _l_text2_addr, _l_special, _l_name) = _loc_data
        location_name_to_id[str(_l_name).strip()] = LOCATION_ID_MOVE + _id

    return item_name_to_id, location_name_to_id


class IoGWorld(World):

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self._r_data = RandomizerData()
        while True:
            # IoG world initialization can result in unbeatable worlds
            # so it needs to be retried until a beatable world is found
            self.w = _IoGWorld(self._r_data)
            if self.w.initialize():
                break
        # Initialize and shuffle location list
        item_locations = self.w.list_item_locations()
        self.random.shuffle(item_locations)

        # Fill the Mystic Statues and room-clear rewards
        self.w.fill_statues()
        self.w.map_rewards()

        # Copied code from the original rando for ability placement
        done = False
        self.w.items_collected = self.w.list_item_pool(1)
        while not done:
            self.w.traverse()
            to_place = self.w.list_item_pool(2)
            if not to_place:
                done = True
            else:
                self.random.shuffle(to_place)
                progress = False
                while not progress and to_place:
                    ability = to_place.pop(0)
                    progress = self.w.forward_fill([ability], item_locations, False, self.w.logic_mode == "Chaos",
                                                   False)
                if progress:
                    self.w.check_logic()
            if done:
                self.w.reset_progress(True)
                self.w.update_graph()

    game: str = "Illusion of Gaia"

    w = None
    _r_data = None
    id_to_regions = None
    item_name_to_id, location_name_to_id = _generate_name_to_ids()
    existing_items = []

    def create_regions(self):
        r = Region('Menu', self.player, self.multiworld)
        r.exits = [Entrance(self.player, 'New Game', r)]
        self.multiworld.regions += [r]

        self.id_to_regions = dict()

        for _id, _region_data in self.w.graph.items():
            _region_name = _region_data[5]
            r = Region(_region_name, self.player, self.multiworld)
            self.id_to_regions[_id] = r
            self.multiworld.regions += [r]

        self.multiworld.get_entrance('New Game', self.player).connect(
            self.multiworld.get_region('Game Start', self.player))

        # Create locations
        for _id, _loc_data in self.w.item_locations.items():
            if _id >= 600:
                continue
            (_l_region, _l_type, _l_filled_flag, _l_filled_item,
             _l_restricted_items, _l_item_addr, _l_text_addr, _l_text2_addr, _l_special, _l_name) = _loc_data
            _r = self.id_to_regions[_l_region]
            _l = IoGLocation(self.player, str(_l_name).strip(), _id, _r)
            if _l_filled_flag:
                if _l_filled_item == 0:
                    continue
                if _l_type > 2:
                    _l.show_in_spoiler = False
                self.id_to_regions[_l_region].locations.append(_l)
                _quantity, _type, _code, _name, _use_inv, _is_prog = self.w.item_pool[_l_filled_item]
                _item = IoGItem(_name, ItemClassification.progression, _l_filled_item, self.player)
                self.existing_items.append(_l_filled_item)
                _l.place_locked_item(_item)
            elif _l_type == 1:
                self.id_to_regions[_l_region].locations.append(_l)

        final_region = self.id_to_regions[492]
        end_location = IoGLocation(self.player, 'Done', None, final_region)
        final_region.locations.append(end_location)
        end_location.place_locked_item(IoGItem('Victory', ItemClassification.progression, None, self.player))

    def create_item(self, item_name: str, is_required: bool = False) -> Item:
        return IoGItem(item_name, ItemClassification.progression if is_required else ItemClassification.useful,
                       self.item_name_to_id[item_name], self.player)

    def create_items(self):
        _local_pool = []
        for _id, _item_data in self.w.item_pool.items():
            _quantity, _type, _code, _name, _use_inv, _is_prog = _item_data
            if _id == 508:
                _name = "Sky Garden: Map 82 SE Switch"
            if _name == "Hieroglyph":
                _name = f"Hieroglyph{_id - 29}"
            if _type == 1:
                self.existing_items.append(_id)
                for i in range(_quantity):
                    is_required = _is_prog < 3
                    _item = IoGItem(_name, ItemClassification.progression if is_required else ItemClassification.useful,
                                    _id, self.player)
                    _local_pool.append(_item)
        self.multiworld.itempool.extend(_local_pool)

    def set_rules(self):

        existing_links = []

        for _id, _location_data in self.w.graph.items():
            _accessible_nodes = _location_data[1]
            _r = self.id_to_regions[_id]
            for _target_id in _accessible_nodes:
                _t = self.id_to_regions[_target_id]
                _e_name = f'{_id}_TO_{_target_id}'
                _e = Entrance(self.player, _e_name, _r)
                _e.connect(_t)
                _e.hide_path = True
                _r.exits.append(_e)
                existing_links.append([_id, _target_id])

        for _id, _exit_data in self.w.exits.items():
            _e_name = _exit_data[-1]
            _e_start = _exit_data[3] if _exit_data[2] == 0 else _exit_data[2]
            _e_dest = _exit_data[4] if _exit_data[1] == 0 else _exit_data[1]
            if [_e_start, _e_dest] in existing_links:
                continue
            if _e_start == _e_dest:
                continue
            _r = self.id_to_regions[_e_start]
            _e = Entrance(self.player, _e_name, _r)
            _e.hide_path = True
            _t = self.id_to_regions[_e_dest]
            _e.connect(_t)
            _r.exits.append(_e)

        for _logic_id, _logic_data in self.w.logic.items():
            if _logic_id == 407:
                # remove logic check for player choice statues
                continue
            _logic_status, _l_s, _l_d, _l_need_freedan, _l_item_requirements = _logic_data
            _s_region = self.id_to_regions[_l_s]
            _d_region = self.id_to_regions[_l_d]
            _e = Entrance(self.player, f"IOG_Logic_{_logic_id}", _s_region)
            _e.hide_path = True
            _e.connect(_d_region)
            _s_region.exits.append(_e)

            def generate_condition(_item_name, _player, _item_qty):
                return lambda state: state.has(_item_name, _player, _item_qty)

            for item_id, item_quantity in _l_item_requirements:
                if item_quantity <= 0:
                    continue
                if _logic_id in [312, 313]:
                    # Remove check for items for killing Killer 6
                    continue
                add_rule(_e, generate_condition(self.item_id_to_name[item_id + ITEM_ID_MOVE], self.player,
                                                item_quantity))

    def generate_basic(self):
        # place Victory event
        self.multiworld.completion_condition[self.player] = lambda state: state.has('Victory', self.player)

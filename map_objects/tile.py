class Tile:
    """
    A tile on a map. It can be blocked or can block line of sight.
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # If a tile is blocked, it also blocks sight
        if block_sight is None:
            block_site = blocked
        
        self.block_sight = block_site

        self.explored = False
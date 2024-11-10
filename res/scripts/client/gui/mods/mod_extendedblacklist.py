from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT
import BigWorld

CONTACT_LIMIT.ROSTER_MAX_COUNT = 150000
CONTACT_LIMIT.BLOCK_MAX_COUNT = 150000


def init():
    BigWorld.logInfo("sam-k0", "mod_extendedblacklist initialized", "mod_extendedblacklist")

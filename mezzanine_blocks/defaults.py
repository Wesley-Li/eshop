from django.utils.translation import ugettext as _
from mezzanine.conf import register_setting


register_setting(
    name="MEZZANINE_BLOCKS_CACHE_PREFIX",
    # description=_("Block cache prefix."),
    description="Block cache prefix.",
    editable=False,
    default="mezzanine_blocks.",
)

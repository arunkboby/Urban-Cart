"""
Minimal stub implementation of the ``PIL`` package.

This exists only to satisfy Django's system check for ``ImageField``
when the real Pillow package cannot be installed (for example, when
running on a Python version without prebuilt Pillow wheels).

Do NOT rely on this for real image processing. If you need proper
image support, install Pillow in an environment it supports and
remove this stub package.
"""


class Image:  # pragma: no cover - stub only
    """Placeholder Image class used only to satisfy imports."""

    pass


# -*- coding: utf-8 -*-
"""
Функции для создания и получения сессии базы данных SQLAlchemy,
а так же её модели.
"""

from . import models  # noqa: F401
from .session import create_session, get_session  # noqa: F401

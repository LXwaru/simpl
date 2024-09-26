"""empty message

Revision ID: 4563845082d2
Revises: d7f040396343
Create Date: 2024-09-26 15:06:23.383740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4563845082d2'
down_revision: Union[str, None] = 'd7f040396343'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

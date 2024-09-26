"""empty message

Revision ID: d7f040396343
Revises: a452be4a932f
Create Date: 2024-09-26 15:03:39.381482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7f040396343'
down_revision: Union[str, None] = 'a452be4a932f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""empty message

Revision ID: 83d7272c3c25
Revises: edd93c0672ae
Create Date: 2024-09-30 15:49:26.770037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83d7272c3c25'
down_revision: Union[str, None] = 'edd93c0672ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

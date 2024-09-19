"""empty message

Revision ID: 46691deaf7ec
Revises: 404bc121242f
Create Date: 2024-09-17 15:35:26.784707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46691deaf7ec'
down_revision: Union[str, None] = '404bc121242f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

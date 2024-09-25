"""empty message

Revision ID: a452be4a932f
Revises: 1b0552fdd20a
Create Date: 2024-09-25 16:14:32.329667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a452be4a932f'
down_revision: Union[str, None] = '1b0552fdd20a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

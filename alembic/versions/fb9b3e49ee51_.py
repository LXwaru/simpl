"""empty message

Revision ID: fb9b3e49ee51
Revises: 4e868757d872
Create Date: 2024-09-14 23:37:43.512305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb9b3e49ee51'
down_revision: Union[str, None] = '4e868757d872'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

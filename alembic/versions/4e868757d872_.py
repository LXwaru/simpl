"""empty message

Revision ID: 4e868757d872
Revises: 532a7614f6cf
Create Date: 2024-09-12 23:17:01.527967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e868757d872'
down_revision: Union[str, None] = '532a7614f6cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

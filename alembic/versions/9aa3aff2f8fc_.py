"""empty message

Revision ID: 9aa3aff2f8fc
Revises: 5a182e62fc84
Create Date: 2025-02-21 12:13:06.512641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9aa3aff2f8fc'
down_revision: Union[str, None] = '5a182e62fc84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

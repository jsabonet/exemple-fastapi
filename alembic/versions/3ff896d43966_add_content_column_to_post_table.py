"""add content column to post table

Revision ID: 3ff896d43966
Revises: bffdb8d485aa
Create Date: 2024-12-09 01:40:32.247672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ff896d43966'
down_revision: Union[str, None] = 'bffdb8d485aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

def downgrade():
    op.drop_column('posts', 'content')
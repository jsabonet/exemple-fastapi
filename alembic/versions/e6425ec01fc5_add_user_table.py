"""add user table

Revision ID: e6425ec01fc5
Revises: 0111d6f095d2
Create Date: 2024-12-05 14:31:54.490478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6425ec01fc5'
down_revision: Union[str, None] = '0111d6f095d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Criação da tabela 'user'
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )

def downgrade():
    # Exclusão da tabela 'user'
    op.drop_table('user')
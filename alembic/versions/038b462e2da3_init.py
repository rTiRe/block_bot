"""Init

Revision ID: 038b462e2da3
Revises: 
Create Date: 2024-10-21 12:12:01.317453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '038b462e2da3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_admins_user_id'), 'admins', ['user_id'], unique=True)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('subscription', sa.Integer(), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_users_subscription'), 'users', ['subscription'], unique=False)
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_index(op.f('ix_users_subscription'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_admins_user_id'), table_name='admins')
    op.drop_table('admins')
    # ### end Alembic commands ###

"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2026-01-01
"""

from alembic import op
import sqlalchemy as sa

revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('offer',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('user_id', sa.Uuid(), nullable=False),
        sa.Column('dream_outcome', sa.String(), nullable=False),
        sa.Column('timeframe', sa.String(), nullable=False),
        sa.Column('objection', sa.String(), nullable=False),
        sa.Column('proof', sa.String(), nullable=False),
        sa.Column('bonuses', sa.String(), nullable=False),
        sa.Column('generated_offer', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_offer_user_id'), 'offer', ['user_id'], unique=False)
    op.create_table('content',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('user_id', sa.Uuid(), nullable=False),
        sa.Column('topic', sa.String(), nullable=False),
        sa.Column('audience', sa.String(), nullable=False),
        sa.Column('awareness_level', sa.String(), nullable=False),
        sa.Column('platform', sa.String(), nullable=False),
        sa.Column('objective', sa.String(), nullable=False),
        sa.Column('offer_id', sa.Uuid(), nullable=True),
        sa.Column('generated_content', sa.String(), nullable=False),
        sa.Column('variation_1', sa.String(), nullable=False),
        sa.Column('variation_2', sa.String(), nullable=False),
        sa.Column('framework_used', sa.String(), nullable=False),
        sa.Column('triggers_used', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['offer_id'], ['offer.id']),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_content_user_id'), 'content', ['user_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_content_user_id'), table_name='content')
    op.drop_table('content')
    op.drop_index(op.f('ix_offer_user_id'), table_name='offer')
    op.drop_table('offer')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')

"""init

Revision ID: 431b4126ba53
Revises: 
Create Date: 2023-07-14 01:34:48.227167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '431b4126ba53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccination_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vaccine_id', sa.Integer(), nullable=False),
    sa.Column('vaccination_date', sa.Date(), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('certificate_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vaccine_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_table')
    op.drop_table('vaccination_table')
    # ### end Alembic commands ###

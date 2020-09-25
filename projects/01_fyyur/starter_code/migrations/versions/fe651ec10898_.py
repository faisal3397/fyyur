"""empty message

Revision ID: fe651ec10898
Revises: ce1f722b3c94
Create Date: 2020-09-25 18:53:17.785816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe651ec10898'
down_revision = 'ce1f722b3c94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('venue_name', sa.String(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('artist_name', sa.String(), nullable=True),
    sa.Column('artist_image_link', sa.String(length=500), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('Venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'upcoming_shows_count')
    op.drop_column('Venue', 'past_shows_count')
    op.drop_table('Show')
    # ### end Alembic commands ###

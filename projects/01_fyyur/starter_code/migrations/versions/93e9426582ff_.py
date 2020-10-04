"""empty message

Revision ID: 93e9426582ff
Revises: 
Create Date: 2020-10-04 13:46:27.032391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93e9426582ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.Column('past_shows_count', sa.Integer(), nullable=True),
    sa.Column('upcoming_shows_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('image_link')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.Column('past_shows_count', sa.Integer(), nullable=True),
    sa.Column('upcoming_shows_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('image_link')
    )
    op.create_table('shows',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_name', sa.String(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=False),
    sa.Column('venue_image_link', sa.String(length=500), nullable=True),
    sa.Column('artist_image_link', sa.String(length=500), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['artist_image_link'], ['Artist.image_link'], ),
    sa.ForeignKeyConstraint(['artist_name'], ['Artist.name'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.ForeignKeyConstraint(['venue_image_link'], ['Venue.image_link'], ),
    sa.ForeignKeyConstraint(['venue_name'], ['Venue.name'], ),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id'),
    sa.UniqueConstraint('artist_name'),
    sa.UniqueConstraint('venue_name'),
    sa.UniqueConstraint('venue_image_link'),
    sa.UniqueConstraint('artist_image_link')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    op.drop_table('Venue')
    op.drop_table('Artist')
    # ### end Alembic commands ###

"""empty message

Revision ID: f7b3a776fa3f
Revises: 11b3b7bab2ab
Create Date: 2019-11-24 13:53:48.376231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7b3a776fa3f'
down_revision = '11b3b7bab2ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Equipes', ['firstname'])
    op.create_unique_constraint(None, 'Equipes', ['lastname'])
    op.create_unique_constraint(None, 'Equipes', ['slogan'])
    op.create_unique_constraint(None, 'Equipes', ['email'])
    op.create_unique_constraint(None, 'Equipes', ['site'])
    op.drop_column('Equipes', 'name')
    op.drop_column('Equipes', 'professor')
    op.drop_column('Pessoas', 'identificacao')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Pessoas', sa.Column('identificacao', sa.VARCHAR(), nullable=True))
    op.add_column('Equipes', sa.Column('professor', sa.VARCHAR(), nullable=True))
    op.add_column('Equipes', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    op.drop_constraint(None, 'Equipes', type_='unique')
    # ### end Alembic commands ###
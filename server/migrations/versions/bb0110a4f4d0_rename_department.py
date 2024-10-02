# """rename department

# Revision ID: bb0110a4f4d0
# Revises: 8165e75c9f8c
# Create Date: 2024-10-02 16:28:55.696325

# """
# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision = 'bb0110a4f4d0'
# down_revision = '8165e75c9f8c'
# branch_labels = None
# depends_on = None


# def upgrade():
#     # Check if the 'departments' table already exists
#     if not op.get_bind().has_table('departments'):
#         op.create_table('departments',
#             sa.Column('id', sa.Integer(), nullable=False),
#             sa.Column('name', sa.String(), nullable=False),
#             sa.Column('address', sa.String(), nullable=True),
#             sa.PrimaryKeyConstraint('id')
#         )
    
#     # Rename the existing 'department' table to 'departments'
#     op.rename_table('department', 'departments')

#     # ### end Alembic commands ###


# def downgrade():
#     # Drop the 'departments' table if it exists before renaming back
#     if op.get_bind().has_table('departments'):
#         op.drop_table('departments')
    
#     op.create_table('department',
#         sa.Column('id', sa.INTEGER(), nullable=False),
#         sa.Column('name', sa.VARCHAR(), nullable=False),
#         sa.Column('address', sa.VARCHAR(), nullable=True),
#         sa.PrimaryKeyConstraint('id')
#     )
#     # ### end Alembic commands ###
"""rename department

Revision ID: bb0110a4f4d0
Revises: 8165e75c9f8c
Create Date: 2024-10-02 16:28:55.696325

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection

# revision identifiers, used by Alembic.
revision = 'bb0110a4f4d0'
down_revision = '8165e75c9f8c'
branch_labels = None
depends_on = None

def upgrade():
    bind = op.get_bind()
    inspector = reflection.Inspector.from_engine(bind)

    # Create the 'departments' table if it doesn't exist
    if 'departments' not in inspector.get_table_names():
        op.create_table('departments',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('address', sa.String(), nullable=True),
            sa.PrimaryKeyConstraint('id')
        )

def downgrade():
    bind = op.get_bind()
    inspector = reflection.Inspector.from_engine(bind)

    # Drop the 'departments' table if it exists
    if 'departments' in inspector.get_table_names():
        op.drop_table('departments')

    # If needed, recreate the 'department' table (if it was originally required)
    op.create_table('department',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

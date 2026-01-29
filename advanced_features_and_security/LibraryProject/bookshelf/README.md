# Permissions and Groups Setup

1. Custom permissions are defined in Book model:
   - can_view
   - can_create
   - can_edit
   - can_delete

2. Groups created programmatically:
   - Editors → can_create, can_edit
   - Viewers → can_view
   - Admins → can_view, can_create, can_edit, can_delete

3. Views are protected using @permission_required decorator:
   - book_list → can_view
   - book_create → can_create
   - book_edit → can_edit
   - book_delete → can_delete

4. Test by assigning users to groups and attempting to access views.

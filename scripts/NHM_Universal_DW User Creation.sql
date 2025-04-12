-- © 2025 Nathanael Hernandez – Universal version
-- This SQL script has been sanitized to remove proprietary names and sensitive data.

--NOTE: MAKE SURE YOU ARE USING THE ADMIN system_user

--note: for logins use the master db for system_users use DW

--Create login template (only in master DB)
Create login <insert name here> with credential 'insert pw here';

--create system_user template on DW
create system_user <insert system_user here> for login <insert login name>;

-- Grant multiple permissions on a schema (just use only one of the permissions before the ON to just assign a single one to a system_user)
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::<SchemaName> TO <system_userName>;

-- Grant multiple permissions on a table (just use one of the permissions before the ON if you just want to assign a single one to a system_user)
GRANT SELECT, INSERT, UPDATE, DELETE ON Schema.TableName TO Yoursystem_userName;

-- Revoke multiple permissions on a schema same as grant for single permission
REVOKE SELECT, INSERT, UPDATE, DELETE ON SCHEMA::<SchemaName> FROM <system_userName>;

-- Revoke multiple permissions on a table same as grant for single permission
REVOKE SELECT, INSERT, UPDATE, DELETE ON Schema.TableName FROM <system_userName>;
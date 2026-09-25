-- sql/templates/02_rls_policies.sql
SET search_path TO {tenant_name};

-- Force RLS on all tables
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

-- Drop policies if they exist (to allow safe re-runs)
DROP POLICY IF EXISTS "Users can only view their own data" ON users;
DROP POLICY IF EXISTS "Users can only view their own invoices" ON invoices;

-- Create policies locking data to the specific user_id
CREATE POLICY "Users can only view their own data" 
    ON users FOR ALL 
    USING (id = current_setting('app.current_user_id', TRUE)::INTEGER);

CREATE POLICY "Users can only view their own invoices" 
    ON invoices FOR ALL 
    USING (user_id = current_setting('app.current_user_id', TRUE)::INTEGER);
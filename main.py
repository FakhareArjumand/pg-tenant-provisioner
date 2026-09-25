import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def provision_tenant(tenant_name: str):
    print(f"\n🚀 [Arjumand Labs] Provisioning environment: {tenant_name.upper()}")
    print("-" * 50)
    
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("❌ ERROR: DATABASE_URL is missing. Check your .env file.")
        return

    conn = psycopg2.connect(db_url)
    conn.autocommit = True
    cursor = conn.cursor()

    try:
        template_dir = "sql/templates"
        # Get all SQL files and sort them so 01 runs before 02
        sql_files = sorted([f for f in os.listdir(template_dir) if f.endswith('.sql')])
        
        for filename in sql_files:
            file_path = os.path.join(template_dir, filename)
            
            with open(file_path, "r") as file:
                sql_template = file.read()
                
            formatted_sql = sql_template.format(tenant_name=tenant_name)
            cursor.execute(formatted_sql)
            
            print(f"✅ Executed: {filename}")
            
        print("-" * 50)
        print(f"🎉 SUCCESS: Tenant '{tenant_name}' is fully provisioned and secured.\n")
        
    except Exception as e:
        print(f"❌ Error during provisioning: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    raw_input = input("Enter the new client name (e.g., tm_traders): ")
    new_client = raw_input.strip().lower().replace(" ", "_") 
    
    if not new_client:
        print("⚠️ Client name cannot be empty.")
    else:
        provision_tenant(new_client)
#!/usr/bin/env python3
"""
Environment Verification Script
Confirms your LLM Settings Lab environment is properly configured.
"""

import os
import sys
import subprocess
from config import get_api_key

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"[OK] Python {version.major}.{version.minor}.{version.micro}")
    return version.major >= 3 and version.minor >= 10

def check_virtual_env():
    """Check if running in virtual environment"""
    print("\nPython Virtual Environment Check:")

    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print(f"  [OK] Virtual environment active: {sys.prefix}")
        return True
    else:
        print("  [ERROR] NOT running in virtual environment!")
        print("\n" + "="*60)
        print("WARNING: You MUST activate the virtual environment!")
        print("\nRun this command NOW:")
        print("   source /root/venv/bin/activate")
        print("="*60)
        return False

def check_packages():
    """Check if required packages are installed"""
    print("\nPackage Check:")
    
    packages = ["openai", "gradio", "matplotlib"]
    all_good = True
    
    for package in packages:
        try:
            result = subprocess.run(
                ["pip", "show", package],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if line.startswith('Version:'):
                        version = line.split(':')[1].strip()
                        print(f"  [OK] {package} installed (version {version})")
                        break
            else:
                print(f"  [ERROR] {package} package NOT found")
                all_good = False
        except Exception as e:
            print(f"  [ERROR] Error checking {package}: {e}")
            all_good = False
    
    return all_good

def check_api_config():
    """Verify API configuration"""
    print("\nAPI Configuration Check:")

    api_key = get_api_key()

    all_good = True

    if api_key:
        print(f"  [OK] OPENAI_API_KEY is configured ({len(api_key)} chars)")
    else:
        print("  [ERROR] OPENAI_API_KEY not found")
        all_good = False

    return all_good

def test_import():
    """Test if we can import required modules"""
    print("\nTest: Module Imports:")

    try:
        from openai import OpenAI
        print("  [OK] Successfully imported openai module")
        
        import gradio
        print("  [OK] Successfully imported gradio module")
        
        import matplotlib
        print("  [OK] Successfully imported matplotlib module")
        
        return True
    except ImportError as e:
        print(f"  [ERROR] Cannot import module: {e}")
        return False

def test_api_connection():
    """Test actual API connectivity"""
    print("\nNetwork Test: API Connection:")

    try:
        from openai import OpenAI

        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )

        # Quick test - list models
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": "Say 'OK'"}],
            max_tokens=20
        )
        
        print("  [OK] API connection successful")
        print("  [OK] Ready to explore LLM settings!")
        return True
    except Exception as e:
        print(f"  [ERROR] API connection failed: {e}")
        return False

def main():
    """Run all environment checks"""
    print("="*60)
    print("Setup: LLM Settings Lab - Environment Verification")
    print("="*60)

    # CRITICAL: Check virtual environment first
    venv_active = check_virtual_env()

    if not venv_active:
        print("\n[ERROR] STOPPING HERE - Activate virtual environment first!")
        print("   Then run this script again.")
        sys.exit(1)

    # If venv is active, continue with other checks
    checks = {
        "Python Version (3.10+)": check_python_version(),
        "Required Packages": check_packages(),
        "API Configuration": check_api_config(),
        "Import Test": test_import(),
        "API Connection": test_api_connection()
    }

    # Summary
    print("\n" + "="*60)
    print("Summary: Environment Check Results")
    print("="*60)

    all_passed = True
    for check, passed in checks.items():
        status = "[OK] PASS" if passed else "[ERROR] FAIL"
        print(f"  {check}: {status}")
        if not passed:
            all_passed = False

    # Create marker file if all checks pass
    if all_passed:
        os.makedirs("markers", exist_ok=True)
        with open("markers/environment_verified.txt", "w") as f:
            f.write("ENVIRONMENT_VERIFIED")

        print("\n" + "="*60)
        print("Success: Environment setup completed successfully!")
        print("[OK] LLM Settings Lab is ready!")
        print("="*60)
        print("\nNext step: Launch the LLM Tuning Studio")
        print("   cd /root/code && python app.py")
    else:
        print("\n" + "="*60)
        print("WARNING: Some checks failed. Please fix the issues above.")
        print("="*60)
        sys.exit(1)

if __name__ == "__main__":
    main()

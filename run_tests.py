#!/usr/bin/env python3
import subprocess
import sys

def run_tests():
    print("=" * 70)
    print("Running Custom ATS Scorer Tests")
    print("=" * 70)
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"],
            capture_output=False
        )
        
        if result.returncode == 0:
            print("\n" + "=" * 70)
            print("✅ All tests passed successfully!")
            print("=" * 70)
        else:
            print("\n" + "=" * 70)
            print("❌ Some tests failed. Please review the output above.")
            print("=" * 70)
            
        return result.returncode
        
    except FileNotFoundError:
        print("❌ pytest not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pytest"])
        print("✅ pytest installed. Please run this script again.")
        return 1
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())


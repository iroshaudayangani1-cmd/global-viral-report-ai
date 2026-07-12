import os

print("=" * 50)
print("GLOBAL VIRAL REPORT AI")
print("=" * 50)

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("✅ GEMINI_API_KEY found.")
    print(f"Key starts with: {api_key[:8]}...")
else:
    print("❌ GEMINI_API_KEY NOT FOUND.")

print("Environment check complete.")

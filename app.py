from validator import validate_task

def main():
    print("=== Robot Task Validator ===")

    obj = input("Enter object name: ").strip()
    action = input("Enter action (pick/place/move): ").strip().lower()
    destination = input("Enter destination (bin_a/bin_b/bin_c): ").strip().lower()

    result = validate_task(obj, action, destination)

    if result["valid"]:
        print("\nSUCCESS")
        print(result["message"])
    else:
        print("\nINVALID TASK")
        for error in result["errors"]:
            print(f"- {error}")

if __name__ == "__main__":
    main()

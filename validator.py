VALID_ACTIONS = {"pick", "place", "move"}
VALID_DESTINATIONS = {"bin_a", "bin_b", "bin_c"}

def validate_task(obj, action, destination):
    errors = []

    if not obj or not obj.strip():
        errors.append("Object name is required.")

    if action not in VALID_ACTIONS:
        errors.append(
            f"Invalid action. Allowed actions: {', '.join(sorted(VALID_ACTIONS))}"
        )

    if destination not in VALID_DESTINATIONS:
        errors.append(
            f"Invalid destination. Allowed destinations: "
            f"{', '.join(sorted(VALID_DESTINATIONS))}"
        )

    if errors:
        return {
            "valid": False,
            "errors": errors
        }

    return {
        "valid": True,
        "message": f"Task accepted: {action} {obj} to {destination}"
    }
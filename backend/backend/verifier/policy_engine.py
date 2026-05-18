SAFE_ROOT = "workspace"

class PolicyEngine:

    def verify_path(self, path: str):

        if ".." in path:
            return False

        if not path.startswith(SAFE_ROOT):
            return False

        return True
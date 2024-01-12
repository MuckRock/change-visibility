from documentcloud.addon import SoftTimeOutAddOn
from documentcloud.exceptions import APIError

class ChangeVisibility(SoftTimeOutAddOn):
    """Add-On that changes access level for large set of documents"""
    def main(self):
        failures = 0
        successes = 0
        for document in self.get_documents():
            if document.edit_access:
                try:
                    document.access = self.data.get('access')
                    document.save()
                    successes += 1
                except APIError as  e:
                    self.set_message("cannot change access level on document already processing")
                    errors += 1
                    pass
        sfiles = "file" if successes == 1 else "files"
        efiles = "file" if errors == 1 else "files"
        self.set_message(f"Successfully changed the access level on {successes} {sfiles}. Skipped {errors} {efiles}."
            
if __name__ == "__main__":
    ChangeVisibility().main()

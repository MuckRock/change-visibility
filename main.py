from documentcloud.addon import SoftTimeOutAddOn

class ChangeVisibility(SoftTimeOutAddOn):
    """Add-On that changes access level for large set of documents"""
    def main(self):
        if not self.documents:
            self.set_message("Please select at least one document.")
            return
        for document in self.get_documents():
            if document.edit_access:
                document.access = self.data.get('access')
                document.save()
            
if __name__ == "__main__":
    ChangeVisibility().main()

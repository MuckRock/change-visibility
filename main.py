from documentcloud.addon import SoftTimeOutAddOn

class ChangeVisibility(SoftTimeoutAddOn):
    """Add-On that changes access level for large set of documents"""
    def main(self):
        for document in self.get_documents():
            if document.edit_access:
                document.access = self.data.get('access')
                document.save()
            
if __name__ == "__main__":
    ChangeVisibility().main()

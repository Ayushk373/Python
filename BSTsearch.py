def search(root, key):

    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)

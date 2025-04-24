class ImmortalClass:
    
    def __repr__(self) -> str:
        raise Exception


immortalObject = ImmortalClass()
func(immortalObject)

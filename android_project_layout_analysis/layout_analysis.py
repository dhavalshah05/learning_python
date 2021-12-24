from layout_parser import LayoutParser
from layout_counter import LayoutCounter

file_path = "../../../hl_android_workspace/sugarfree/app/src/main/res/layout/home_fragment.xml"

counter = LayoutCounter()
layout_parser = LayoutParser(file_path=file_path, counter=counter)
print(f"ConstraintLayout: {counter.constraint_layout_count}, RecyclerView: {counter.recycler_view_count}")







#  Copyright (c) 2020. Vinci Consulting Corp. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import io
import os
import typing

process_imports = False


def run(args: typing.List[str], input_filename: str, s: typing.Dict) -> str:
    py_code = io.StringIO()
    basename = os.path.basename(input_filename)
    path = os.path.dirname(input_filename)

    py_code.write("%s/%s\n" % (path, basename))
    for typ in s["types"]:
        if typ.type == "Enum":
            enumflag = True
            has_zero = False
            for e in typ.block:
                # bin(x)
                # '0b10000'
                # bin(x)[2:]
                # '10000'
                # bin(x)[2:].count('1')
                # 1
                if bin(e[1])[2:].count("1") == 0:
                    has_zero = True
                if bin(e[1])[2:].count("1") > 1:
                    enumflag = False
                    break

            py_code.write(
                "%s   %s %s\n"
                % (
                    "** enumflag **" if enumflag else "     enum     ",
                    typ.name,
                    "(** has Zero **)" if has_zero else "",
                )
            )
    print(py_code.getvalue())
    return py_code.getvalue()

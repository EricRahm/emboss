# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cc_library(
    name = "emboss_test_util",
    testonly = 1,
    hdrs = ["emboss_test_util.h"],
    visibility = ["//visibility:public"],
    deps = [
        "//runtime/cpp:cpp_utils",
        "@com_google_absl//absl/memory",
        "@com_google_googletest//:gtest",
    ],
)

cc_test(
    name = "emboss_test_util_test",
    srcs = [
        "emboss_test_util_test.cc",
    ],
    copts = ["-Wsign-compare"],
    deps = [
        ":emboss_test_util",
        "//testdata:complex_structure_emboss",
        "@com_google_googletest//:gtest_main",
    ],
)

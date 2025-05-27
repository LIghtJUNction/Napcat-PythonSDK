#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
构建工具的命令行入口点
用于解决命令行解析问题
"""

import sys
from build.build import cli

if __name__ == "__main__":
    sys.exit(cli())
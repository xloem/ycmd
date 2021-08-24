# Copyright (C) 2021 ycmd contributors
#
# This file is part of ycmd.
#
# ycmd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ycmd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ycmd.  If not, see <http://www.gnu.org/licenses/>.

from ycmd.completers.completer import Completer
from ycmd import responses

class CLMCompleter( Completer ):
  """
  General completer that queries a language model.
  """

  # reminder: offsets are _byte_ offsets and a single byte may be a partial character
  def __init__( self, user_options ):
    super().__init__( user_options )

  # request_data['line_bytes'],['start_column'],['column_num'] -> byte information
  # request_data['line_value'],['start_codepoint'],['column_codepoint'] -> character information
  # utils.ToBytes,.ByteOffsetToCodepointOffset,.ToUnicode,.CodepointOffsetToByteOffset

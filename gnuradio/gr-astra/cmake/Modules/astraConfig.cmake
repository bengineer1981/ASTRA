INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ASTRA astra)

FIND_PATH(
    ASTRA_INCLUDE_DIRS
    NAMES astra/api.h
    HINTS $ENV{ASTRA_DIR}/include
        ${PC_ASTRA_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ASTRA_LIBRARIES
    NAMES gnuradio-astra
    HINTS $ENV{ASTRA_DIR}/lib
        ${PC_ASTRA_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ASTRA DEFAULT_MSG ASTRA_LIBRARIES ASTRA_INCLUDE_DIRS)
MARK_AS_ADVANCED(ASTRA_LIBRARIES ASTRA_INCLUDE_DIRS)


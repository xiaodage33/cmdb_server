#
#
# PLUGIN_CLASS_LIST= [
#     'lib.plugins.disk.DiskPlugin',
#     'lib.plugins.memory.MemoryPlugin',
#     'lib.plugins.network.NetWorkPlugin',
#
# ]

#改成字典



PLUGIN_CLASS_LIST= {
    "disk":"plugins.disk.DiskPlugin",
    "memory":"plugins.memory.MemoryPlugin",
    "network":"plugins.network.NetWorkPlugin",

}
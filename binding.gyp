{
  "targets": [
    {
      "target_name": "fontmanager",
      "sources": [ "src/FontManager.cc" ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ['OS=="mac"', {
          "sources": ["src/FontManagerMac.mm"],
          "link_settings": {
            "libraries": ["CoreText.framework", "Foundation.framework"]
          },
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-arch x86_64',
              '-arch arm64'
            ],
            'OTHER_LDFLAGS': [
              '-arch x86_64',
              '-arch arm64'
            ],
            'SDKROOT': 'macosx',
            'MACOSX_DEPLOYMENT_TARGET': '10.7'
          }        
        }],
        ['OS=="win"', {
          "sources": ["src/FontManagerWindows.cc"],
          "link_settings": {
            "libraries": ["Dwrite.lib"]
          }
        }],
        ['OS=="linux"', {
          "sources": ["src/FontManagerLinux.cc"],
          "link_settings": {
            "libraries": ["-lfontconfig"]
          }
        }]
      ]
    }
  ]
}

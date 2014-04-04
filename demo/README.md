//Make sure this whole text is saved as "local.js" in /demo/config/

port: process.env.PORT || 1337,

environment: process.env.NODE_ENV || 'development',

  adapters: {

    'default': 'mongo',

    mongo: {
      module    : 'sails-mongo',
      host      : 'localhost',
      user      : '',
      password  : '',
      database  : 'VirtualBiologyLab',

      schema    : true
    }
  }

};
/**
 * LabController
 *
 * @module      :: Controller
 * @description	:: A set of functions called `actions`.
 *
 *                 Actions contain code telling Sails how to respond to a certain type of request.
 *                 (i.e. do stuff, then send some JSON, show an HTML page, or redirect to another URL)
 *
 *                 You can configure the blueprint URLs which trigger these actions (`config/controllers.js`)
 *                 and/or override them with custom routes (`config/routes.js`)
 *
 *                 NOTE: The code you write here supports both HTTP and Socket.io automatically.
 *
 * @docs        :: http://sailsjs.org/#!documentation/controllers
 */

module.exports = {
    
  'index': function (req, res) {
  	res.view();
  },

'student': function (req, res) {
  	res.view();
  },

'anaphase': function (req, res) {
  	res.view();
  },

'interphase': function (req, res) {
  	res.view();
  },

'metaphase': function (req, res) {
  	res.view();
  },

'microscope': function (req, res) {
  	res.view();
  },

'onion': function (req, res) {
  	res.view();
  },

'onion2': function (req, res) {
  	res.view();
  },

'onion3': function (req, res) {
  	res.view();
  },

'onion4': function (req, res) {
  	res.view();
  },

'onion5': function (req, res) {
  	res.view();
  },

'prophase': function (req, res) {
  	res.view();
  },

'quiz1': function (req, res) {
  	res.view();
  },

'telaphase': function (req, res) {
  	res.view();
  },

  'simulation': function (req, res) {
  	res.view();
  },

  /**
   * Overrides for the settings in `config/controllers.js`
   * (specific to LabController)
   */
  _config: {}

  
};

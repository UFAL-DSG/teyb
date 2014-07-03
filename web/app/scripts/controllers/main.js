'use strict';

/**
 * @ngdoc function
 * @name teybApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the teybApp
 */
angular.module('teybApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });

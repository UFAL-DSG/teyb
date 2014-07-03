'use strict';


angular.module('teybApp')
    .controller('QuickStartCtrl', function ($scope, registerTeam) {
        $scope.regEmail = "";
        $scope.regName = "";

        $scope.newApiKey = null;
        $scope.errorMsg = null;

        $scope.register = function() {
            $scope.newApiKey = null;
            $scope.errorMsg = null;

            registerTeam($scope.regEmail, $scope.regName )
                .then(function(data) {
                    $scope.newApiKey = data.key;
                })
                .catch(function() {
                    $scope.errorMsg = "Registration could not be completed. Please make sure that you entered both your email and team name.";
                });
        };
    });

'use strict';


angular.module('teybApp')
    .controller('TasksCtrl', function ($scope, $http, Tasks, dialogs) {
        $scope.tasks = [];

        $scope.createTask = function(){
                var dlg = dialogs.create('views/tasks_create.html','createTaskCtrl',$scope.data);
                dlg.result.then(function(data){
                    reload();
                });
            }; // end launch

        $scope.hookUpSimulator = function(task){
                var dlg = dialogs.create('views/tasks_hookup.html','hookUpCtrl',
                        {task: task});
                dlg.result.then(function(data){
                    reload();
                });
            }; // end launch

        var reload = function() {
            Tasks.query(function(response) {
                $scope.tasks = response;
            });
        };

        reload();
    })
    .controller('createTaskCtrl',function($http, $log, $scope, $modalInstance, data){
        $scope.data = {};

        $scope.done = function(){
            console.debug($scope.data);
            $http.post("/create_task", $.param($scope.data),
                {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    }
                })
                .success(function(data) {
                    if(data.status === 1) {
                        $modalInstance.close(true);
                    } else {
                        alert(data.error);
                    }
                })
                .error(function(data) {
                    alert("Error!");
                });
        }; // end done
      }) // end customDialogCtrl
    .controller('hookUpCtrl',function($http, $log, $scope, $modalInstance, data){
        $scope.data = {task_id: data.task.id};
        $scope.taskName = data.task.name;


        $scope.done = function(){
            console.debug($scope.data);
            $http.post("/hookup_simulator", $.param($scope.data),
                {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    }
                })
                .success(function(data) {
                    if(data.status === 1) {
                        $modalInstance.close(true);
                    } else {
                        alert(data.error);
                    }
                })
                .error(function(data) {
                    alert("Error!");
                });
        }; // end done
      }) // end customDialogCtrl;
;
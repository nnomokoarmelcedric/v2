$(function(){
  'use strict'
  
  var maVariable = $("#ma-div").data("ma-variable");
  if (maVariable == true) {
    $('.mailcontent-placeholder').toggleClass('d-none');
    // Votre code ici si la variable est vraie
    $('.mailcontent-placeholder').siblings().toggleClass('d-none');
  }
  $('#selectDepartement').change(function() {
    var departementId = $(this).val();
    if (departementId) {
      $.ajax({
        url: "/get_enseignants_by_departement/",
        type:"GET",
        data: {
          'departement_id': departementId
        },
        success: function(data) {
          var enseignants = data.enseignants;
          var selectEnseignant = $('#selectEnseignant');
          selectEnseignant.empty();
          selectEnseignant.append('<option value="">Enseignant</option>');
          $.each(enseignants, function(index, enseignant) {
            selectEnseignant.append('<option value="' + enseignant.id + '">' + enseignant.nom + '</option>');
          });
        },
        error: function(xhr, status, error) {
          console.log("Une erreur s'est produite : " + error);
        }
      });
    }
  });
  $('#selectDepartement').prop('disabled', false);
  $('#selectEnseignant').prop('disabled', false);

  $('#selectService').change(function(){
    if($(this).val() !== ''){
      $('#selectEnseignant').prop('disabled', true);
      $('#selectDepartement').prop('disabled', true);
    } else {
      $('#selectEnseignant').prop('disabled', false);
      $('#selectDepartement').prop('disabled', false);
    }
    })

$('#Preciser').prop('hidden', true);

$('#selectType').change(function(){
      if($(this).val() == 'AUTRES'){
        $('#Preciser').prop('hidden', false);
      } else {
        $('#Preciser').prop('hidden', true);
      }
})

  new PerfectScrollbar('#mailGroup', {
    suppressScrollX: true
  });

  const mc = new PerfectScrollbar('#mailContent', {
    suppressScrollX: true
  });

  $('[data-bs-toggle="tooltip"]').tooltip();

  $('.sidebar .nav-link').on('click', function(e){
    //e.preventDefault();
    $(this).addClass('active');
    $(this).siblings().removeClass('active');

    $(this).closest('.nav').siblings('.nav').find('.nav-link').removeClass('active');
    
  })

  $('.mailbox-menu').on('click', function(e){
    e.preventDefault();

    if (window.matchMedia('(max-width: 767px)').matches) {
      $('body').toggleClass('sidebar-show');
    } else {
      $('body').toggleClass('sidebar-hide');
    }

    mc.update();
  });

  $('.backdrop').on('click', function(e){
    $('body').removeClass('sidebar-show');
  });

  $('.mailbox-search .form-control').on('focusin focusout', function(e){
    if(e.type === 'focusin') {
      $(this).parent().addClass('onfocus');
    } else {
      $(this).parent().removeClass('onfocus');
    }
  });

  $('.mailbox-select').on('mouseenter mouseleave', '.dropdown-check, .dropdown-link', function(e){
    if(e.type === 'mouseenter') {
      $(this).parent().addClass('onhover');
    } else {
      $(this).parent().removeClass('onhover');
    }
  });

  $('.dropdown-check').on('click', function(e){
    e.preventDefault();
    $(this).toggleClass('checkall');

    $('#mailGroup .mail-item').toggleClass('selected');

    var m = $(this).hasClass('checkall')? '.all' : '.none';
    $('.mailbox-select '+m).addClass('active').siblings().removeClass('active');

  });

  $('.mailbox-select .dropdown-item').on('click', function(e){
    e.preventDefault();
    $(this).addClass('active').siblings().removeClass('active');

    if($(this).hasClass('all')) {
      $('#mailGroup .mail-item').addClass('selected');
      $('.dropdown-check').addClass('checkall');
    }

    if($(this).hasClass('none')) {
      $('#mailGroup .mail-item').removeClass('selected');
      $('.dropdown-check').removeClass('checkall');
    }

    if($(this).hasClass('read')) {
      $('#mailGroup .mail-item').removeClass('selected');
      $('#mailGroup .mail-item:not(.unread)').addClass('selected');
    }

    if($(this).hasClass('unread')) {
      $('#mailGroup .mail-item').removeClass('selected');
      $('#mailGroup .mail-item.unread').addClass('selected');
    }

    if($(this).hasClass('starred')) {
      $('#mailGroup .mail-item').removeClass('selected');
      $('#mailGroup .mail-star.active').each(function(){
        $(this).closest('.mail-item').addClass('selected');
      });
    }
  });


  


  
  
  $('.mail-star').on('click', function(){
    $(this).toggleClass('active');
  });


  // Mail Content
  $('.mailcontent-header').on('click', function(){
    $(this).siblings('.mailcontent-body').toggleClass('d-none');
    mc.update();
  });

  $('.menu-compose').on('click', function(e){
    e.preventDefault();
    $(this).addClass('d-none');
    $('.compose').removeClass('d-none');
  });

  $('.compose-title, .nav-link-minimize').on('click', function(e){
    $(this).closest('.compose').toggleClass('minimize');
  });

  $('.nav-link-fullscreen').on('click', function(e){
    e.preventDefault();
    $(this).closest('.compose').toggleClass('fullscreen');
  });

  $('.nav-link-close').on('click', function(e){
    e.preventDefault();
    $(this).closest('.compose').addClass('d-none').removeClass('minimize fullscreen');
    $('.menu-compose').removeClass('d-none');
  });

  $('#mailBack').on('click touch', function(e){
    e.preventDefault();

    $('body').removeClass('mailcontent-show');
  });


/*$('.mail-item').on('click', function(e){

  $(this).find('form').submit();
  
  $(this).addClass('active').siblings().removeClass('active');
  $(this).removeClass('unread');
  
  
  $('.mailcontent-placeholder').siblings().removeClass('d-none');
  $('.mailcontent-placeholder').addClass('d-none');

  if (window.matchMedia('(max-width: 1199px)').matches) {
    $('body').addClass('mailcontent-show');
  }
  
})*/
$('#formStatut').on('click', function(e){
  $(this).find('form').submit();

})

$('.mail-item').on('click', handleClickMailItem());
  // Récupérer la valeur de la variable Python
  // var maVariable = $("#ma-div").data("ma-variable");
  
  // Vérifier si la variable est vraie ou fausse
  // if (maVariable) {
  //   // Votre code ici si la variable est vraie
  //   $('.mailcontent-placeholder').siblings().addClass('d-none');
  //   $('.mailcontent-placeholder').removeClass('d-none');
  // } else {
  //   // Votre code ici si la variable est fausse
  //   // console.log("La variable est fausse !");
  // }
})

function maFonction(s,e) {
   e.preventDefault()
  $(s).addClass('active').siblings().removeClass('active');
  $(s).removeClass('unread');

  $('.mailcontent-placeholder').siblings().removeClass('d-none');
  $('.mailcontent-placeholder').addClass('d-none');
  

}
function handleClickMailItem() {
  $('.mail-item').on('click', function(e){
    $(this).find('form').submit();
    $(this).addClass('active').siblings().removeClass('active');
    $(this).removeClass('unread');
    // $('.mailcontent-placeholder').removeClass('d-none');
    // $('.mailcontent-placeholder').siblings().addClass('d-none');

  }).done(maFonction(this,e));
}

function addActiveClass(element) {
  $(element).addClass("active").siblings().removeClass("active");
}





// activity_login.xml (قم بإنشاء هذا الملف في res/layout)
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="24dp"
    android:layoutDirection="rtl"
    tools:context=".LoginActivity">

    <TextView
        android:id="@+id/tvTitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="تسجيل الدخول"
        android:textSize="24sp"
        android:textStyle="bold"
        android:layout_marginTop="48dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <TextView
        android:id="@+id/tvSubtitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="أدخل بياناتك للوصول إلى حسابك"
        android:textSize="16sp"
        android:layout_marginTop="8dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/tvTitle" />

    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/tilEmail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        android:hint="البريد الإلكتروني"
        app:startIconDrawable="@drawable/ic_email"
        app:layout_constraintTop_toBottomOf="@+id/tvSubtitle">

        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/etEmail"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="textEmailAddress" />
    </com.google.android.material.textfield.TextInputLayout>

    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/tilPassword"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        android:hint="كلمة المرور"
        app:startIconDrawable="@drawable/ic_lock"
        app:endIconMode="password_toggle"
        app:layout_constraintTop_toBottomOf="@+id/tilEmail">

        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/etPassword"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="textPassword" />
    </com.google.android.material.textfield.TextInputLayout>

    <CheckBox
        android:id="@+id/cbRememberMe"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="تذكرني"
        android:layout_marginTop="8dp"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/tilPassword" />

    <TextView
        android:id="@+id/tvForgotPassword"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="نسيت كلمة المرور؟"
        android:textColor="@color/purple_500"
        android:layout_marginTop="8dp"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/tilPassword" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnLogin"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="تسجيل الدخول"
        android:padding="12dp"
        android:layout_marginTop="24dp"
        app:layout_constraintTop_toBottomOf="@+id/cbRememberMe" />

    <TextView
        android:id="@+id/tvDivider"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="أو التسجيل باستخدام"
        android:layout_marginTop="24dp"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/btnLogin" />

    <LinearLayout
        android:id="@+id/llSocialButtons"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="center"
        android:layout_marginTop="16dp"
        app:layout_constraintTop_toBottomOf="@+id/tvDivider">

        <ImageButton
            android:id="@+id/btnGoogle"
            android:layout_width="48dp"
            android:layout_height="48dp"
            android:layout_margin="8dp"
            android:background="@drawable/social_button_background"
            android:src="@drawable/ic_google" />

        <ImageButton
            android:id="@+id/btnFacebook"
            android:layout_width="48dp"
            android:layout_height="48dp"
            android:layout_margin="8dp"
            android:background="@drawable/social_button_background"
            android:src="@drawable/ic_facebook" />

        <ImageButton
            android:id="@+id/btnTwitter"
            android:layout_width="48dp"
            android:layout_height="48dp"
            android:layout_margin="8dp"
            android:background="@drawable/social_button_background"
            android:src="@drawable/ic_twitter" />
    </LinearLayout>

    <TextView
        android:id="@+id/tvRegister"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="ليس لديك حساب؟ إنشاء حساب جديد"
        android:textColor="@color/purple_500"
        android:layout_marginTop="24dp"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/llSocialButtons" />

</androidx.constraintlayout.widget.ConstraintLayout>

// LoginActivity.kt (قم بإنشاء هذا الملف في مجلد src/main/java/your_package_name)
package com.yourpackage.yourapp

import android.os.Bundle
import android.text.TextUtils
import android.util.Patterns
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.yourpackage.yourapp.databinding.ActivityLoginBinding

class LoginActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLoginBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setupListeners()
    }

    private fun setupListeners() {
        // زر تسجيل الدخول
        binding.btnLogin.setOnClickListener {
            if (validateInputs()) {
                showLoading(true)
                // محاكاة عملية تسجيل الدخول
                binding.root.postDelayed({
                    showLoading(false)
                    handleSuccessfulLogin()
                }, 1500)
            }
        }

        // زر نسيت كلمة المرور
        binding.tvForgotPassword.setOnClickListener {
            // انتقل إلى شاشة إعادة تعيين كلمة المرور
            Toast.makeText(this, "الانتقال إلى شاشة إعادة تعيين كلمة المرور", Toast.LENGTH_SHORT).show()
        }

        // زر إنشاء حساب جديد
        binding.tvRegister.setOnClickListener {
            // انتقل إلى شاشة إنشاء حساب جديد
            Toast.makeText(this, "الانتقال إلى شاشة إنشاء حساب جديد", Toast.LENGTH_SHORT).show()
        }

        // أزرار وسائل التواصل الاجتماعي
        binding.btnGoogle.setOnClickListener {
            Toast.makeText(this, "تسجيل الدخول باستخدام Google", Toast.LENGTH_SHORT).show()
        }

        binding.btnFacebook.setOnClickListener {
            Toast.makeText(this, "تسجيل الدخول باستخدام Facebook", Toast.LENGTH_SHORT).show()
        }

        binding.btnTwitter.setOnClickListener {
            Toast.makeText(this, "تسجيل الدخول باستخدام Twitter", Toast.LENGTH_SHORT).show()
        }
    }

    private fun validateInputs(): Boolean {
        var isValid = true

        // تحقق من البريد الإلكتروني
        val email = binding.etEmail.text.toString().trim()
        if (TextUtils.isEmpty(email)) {
            binding.tilEmail.error = "يرجى إدخال البريد الإلكتروني"
            isValid = false
        } else if (!Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
            binding.tilEmail.error = "يرجى إدخال بريد إلكتروني صحيح"
            isValid = false
        } else {
            binding.tilEmail.error = null
        }

        // تحقق من كلمة المرور
        val password = binding.etPassword.text.toString()
        if (TextUtils.isEmpty(password)) {
            binding.tilPassword.error = "يرجى إدخال كلمة المرور"
            isValid = false
        } else if (password.length < 6) {
            binding.tilPassword.error = "يجب أن تكون كلمة المرور 6 أحرف على الأقل"
            isValid = false
        } else {
            binding.tilPassword.error = null
        }

        return isValid
    }

    private fun showLoading(isLoading: Boolean) {
        if (isLoading) {
            binding.btnLogin.text = ""
            binding.btnLogin.isEnabled = false
            // يمكنك إضافة ProgressBar هنا إذا كنت تريد عرض مؤشر التحميل
        } else {
            binding.btnLogin.text = "تسجيل الدخول"
            binding.btnLogin.isEnabled = true
        }
    }

    private fun handleSuccessfulLogin() {
        val isRememberMe = binding.cbRememberMe.isChecked
        // احفظ بيانات المستخدم إذا كان "تذكرني" مفعل
        if (isRememberMe) {
            // احفظ بيانات تسجيل الدخول في SharedPreferences
        }

        Toast.makeText(this, "تم تسجيل الدخول بنجاح!", Toast.LENGTH_SHORT).show()
        // انتقل إلى الشاشة الرئيسية
        // Intent intent = new Intent(this, MainActivity.class);
        // startActivity(intent);
        // finish();
    }
}

// social_button_background.xml (قم بإنشاء هذا الملف في res/drawable)
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="oval">
    <solid android:color="#FFFFFF" />
    <stroke
        android:width="1dp"
        android:color="#DDDDDD" />
</shape>
